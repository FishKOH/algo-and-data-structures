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
    using PutLefttStatus = HeadStatus;
    using RemoveStatus = HeadStatus; // для удобства пользователя: Ok_RemovedLastNode
    using ReplaceStatus = HeadStatus;
    using FindStatus = HeadStatus; // для удобства пользователя: Ok_NotFound
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
    virtual PutLefttStatus get_put_left_status() const = 0;
    virtual RemoveStatus get_remove_status() const = 0;
    virtual ReplaceStatus get_replace_status() const = 0;
    virtual FindStatus get_find_status() const = 0;
    virtual GetStatus get_get_status() const = 0;
    virtual RightStatus get_right_status() const = 0;
};
