template <class T>
class AbstractLinkedList {
public:
    enum class HeadStatus {
        NotCalled,
        Ok,
        EmptyList
    };
    using TailStatus = HeadStatus;
    using PutRightStatus = HeadStatus;
    using PutLeftStatus = HeadStatus;
    using RemoveStatus = HeadStatus; // для удобства пользователя можно добавить статус: Ok_RemovedLastNode
    using ReplaceStatus = HeadStatus;
    using FindStatus = HeadStatus; // для удобства пользователя можно добавить статус: Ok_NotFound
    using GetStatus = HeadStatus;

    enum class RightStatus {
        NotCalled,
        Ok,
        EmptyStack,
        CursorOnTail
    };

public:
    //КОМАНДЫ:

    //предусловие: список не пуст
    //постусловие: курсор установлен на первый узел в списке
    virtual void head() = 0;

    //предусловие: список не пуст
    //постусловие: курсор установлен на последний узел в списке
    virtual void tail() = 0;

    //предусловие 1: список не пуст
    //предусловие 2: курсор установлен НЕ на последний узел в списке
    //постусловие: курсор сдвинут на один узел вправо
    virtual void right() = 0;

    //предусловие: список не пуст
    //постусловие 1: добавлен узел с заданным значением справа от курсора
    //постусловие 2: положение курсора не изменилось
    //альтернативное постусловие 2: курсор установлен на новый узел
    //оба варианта постусловия 2 приемлимы
    virtual void put_right(T value) = 0;

    //предусловие: список не пуст
    //постусловие 1: добавлен узел с заданным значением слева от курсора
    //постусловие 2: положение курсора не изменилось
    //альтернативное постусловие 2: курсор установлен на новый узел
    //оба варианта постусловия 2 приемлимы
    virtual void put_left(T value) = 0;

    //предусловие: список не пуст
    //постусловие 1: удалён узел, на который указывал курсор;
    //постусловие 2: курсор смещается к правому соседу, если он есть,
    //    в противном случае курсор смещается к левому соседу, если он есть
    //важный нюанс вытекающий из постусловия 2: если удаляемый узел был единственный,
    //    то курсор не будет установлен на какой-либо узел
    virtual void remove() = 0;

    //постусловие: все узлы в списке удалены
    virtual void clear() = 0;

    //постусловие 1: добавлен узел с заданным значением в хвост списка
    //постусловие 2: положение курсора не изменилось
    //важный нюанс вытекающий из постусловия 2: если список был пуст,
    //    то курсор не был и не будет установлен на какой-либо узел
    //альтернативное постусловие 2: курсор установлен на новый узел
    //первый вариант постусловия 2 сомнителен, в виду указанного нюанса
    virtual void add_tail(T value) = 0;

    //предусловие: список не пуст
    //постусловие: значение текущего узла заменено на новое значение
    virtual void replace(T value) = 0;

    //предусловие: список не пуст
    //постусловие: курсор смещается на следующий узел с искомым значением,
    //    если такой существует, иначе курсор остаётся на месте
    virtual void find(T value) = 0;

    //постусловие 1: все узлы с заданным значением удалены из списка
    //постусловие 2: если текущий узел был удалён, курсор смещается
    //    на следующий узел справа, который не был удалён, если он есть,
    //    в противном случае(удалён текущий и все справа) курсор смещается
    //    к левому соседу, который не был удалён, если он есть
    //важный нюанс вытекающий из постусловия 2: если удалены все узлы,
    //    то курсор не будет установлен на какой-либо узел
    virtual void remove_all(T value) = 0;

    //ЗАПРОСЫ:

    //предусловие: список не пуст
    virtual T get() const = 0;

    virtual unsigned int size() const = 0;
    virtual bool is_head() const = 0;
    virtual bool is_tail() const = 0;
    virtual bool is_value() const = 0;

    //ЗАПРОСЫ-СТАТУСЫ:

    virtual HeadStatus get_head_status() const = 0;
    virtual TailStatus get_tail_status() const = 0;
    virtual PutRightStatus get_put_right_status() const = 0;
    virtual PutLeftStatus get_put_left_status() const = 0;
    virtual RemoveStatus get_remove_status() const = 0;
    virtual ReplaceStatus get_replace_status() const = 0;
    virtual FindStatus get_find_status() const = 0;
    virtual GetStatus get_get_status() const = 0;
    virtual RightStatus get_right_status() const = 0;
};

/*
2.2. Операция tail не сводима к другим операциям(если исходить из эффективной реализации). 
Данная операция устанавливает курсор на последний узел за O(1) по времени, 
а без этой операции установка курсора на последний узел будет производиться за O(N) по времени 
посредством вызова операции right

2.3. Операция поиска всех узлов с заданным значением, выдающая список таких узлов, уже не нужна. 
Вместо этого можно установить курсор на первый узел операцией head, и далее применяя операцию find(значение), 
будут найдены все значения. 
Для удобства пользователя можно расширить статус операции find, статусом NotFound, чтобы легко обнаружить факт окончания поиска.
*/