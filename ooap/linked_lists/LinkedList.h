namespace linked_list {

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
enum class FindStatus {
    NotCalled,
    Ok,
    NotFound,
    EmptyList
};
using GetStatus = HeadStatus;

enum class RightStatus {
    NotCalled,
    Ok,
    EmptyList,
    CursorOnTail
};

template <class T>
class AbstractParentLinkedList {
public:
    //КОМАНДЫ:

    // постусловие: создан новый пустой список
    // конструктор
    // virtual AbstractParentLinkedList() = 0

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
    //[+]альтернативное постусловие 2: курсор установлен на новый узел
    //оба варианта постусловия 2 приемлимы
    virtual void put_right(T value) = 0;

    //предусловие: список не пуст
    //постусловие 1: добавлен узел с заданным значением слева от курсора
    //постусловие 2: положение курсора не изменилось
    //[+]альтернативное постусловие 2: курсор установлен на новый узел
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
    //[+]альтернативное постусловие 2: курсор установлен на новый узел
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

template <class T>
class AbstractLinkedList : virtual public AbstractParentLinkedList<T> {
};

enum class LeftStatus {
    NotCalled,
    Ok,
    EmptyList,
    CursorOnHead
};

template <class T>
class AbstractTwoWayList : virtual public AbstractParentLinkedList<T> {
public:
    //предусловие 1: список не пуст
    //предусловие 2: курсор установлен НЕ на первый узел в списке
    //постусловие: курсор сдвинут на один узел влево
    virtual void left() = 0;

    virtual LeftStatus get_left_status() const = 0;
};

template <class T>
class ParentLinkedList : virtual public AbstractParentLinkedList<T> {
public:
    ParentLinkedList() = default;
    ~ParentLinkedList()
    {
        clear();
    }

    void head() override
    {
        if (not is_value()) {
            head_status_ = HeadStatus::EmptyList;
            return;
        }
        cursor_ = head_;
        head_status_ = HeadStatus::Ok;
    }
    void tail() override
    {
        if (not is_value()) {
            tail_status_ = TailStatus::EmptyList;
            return;
        }
        cursor_ = tail_;
        tail_status_ = TailStatus::Ok;
    }
    void right() override
    {
        if (not is_value()) {
            right_status_ = RightStatus::EmptyList;
            return;
        }
        if (is_tail()) {
            right_status_ = RightStatus::CursorOnTail;
            return;
        }
        cursor_ = cursor_->nextNode;
        right_status_ = RightStatus::Ok;
    }
    void put_right(T value) override
    {
        if (not is_value()) {
            put_right_status_ = PutRightStatus::EmptyList;
            return;
        }
        Node* newNode = new Node(value);
        newNode->nextNode = cursor_->nextNode;
        newNode->prevNode = cursor_;
        if (newNode->nextNode)
            newNode->nextNode->prevNode = newNode;
        cursor_->nextNode = newNode;

        put_right_status_ = PutRightStatus::Ok;
        if (is_tail())
            tail_ = tail_->nextNode;
        cursor_ = cursor_->nextNode; // right()
    }
    void put_left(T value) override
    {
        if (not is_value()) {
            put_left_status_ = PutLeftStatus::EmptyList;
            return;
        }
        Node* newNode = new Node(value);
        newNode->nextNode = cursor_;
        newNode->prevNode = cursor_->prevNode;
        if (newNode->prevNode)
            newNode->prevNode->nextNode = newNode;
        cursor_->prevNode = newNode;

        put_left_status_ = PutLeftStatus::Ok;
        if (is_head())
            head_ = head_->prevNode;
        cursor_ = cursor_->prevNode; // left()
    }
    void remove() override
    {
        if (not is_value()) {
            remove_status_ = RemoveStatus::EmptyList;
            return;
        }
        bool hasNext = cursor_->nextNode;
        bool hasPrev = cursor_->prevNode;
        if (hasNext)
            cursor_->nextNode->prevNode = cursor_->prevNode;
        else // is tail
            tail_ = tail_->prevNode;
        if (hasPrev)
            cursor_->prevNode->nextNode = cursor_->nextNode;
        else // is head
            head_ = head_->nextNode;

        Node* new_cursor;
        if (hasNext)
            new_cursor = cursor_->nextNode;
        else if (hasPrev)
            new_cursor = cursor_->prevNode;

        delete cursor_;
        cursor_ = new_cursor;

        remove_status_ = RemoveStatus::Ok;
    }
    void clear() override
    {
        head();
        while (is_value())
            remove();
        head_ = nullptr;
        tail_ = nullptr;
        cursor_ = nullptr;
    }
    void add_tail(T value) override
    {
        if (not is_value()) {
            head_ = tail_ = cursor_ = new Node(value);
            return;
        }
        tail();
        put_right(value);
    }
    void replace(T value) override
    {
        if (not is_value()) {
            replace_status_ = ReplaceStatus::EmptyList;
            return;
        }
        cursor_->value = value;
        replace_status_ = ReplaceStatus::Ok;
    }
    void find(T value) override
    {
        if (not is_value()) {
            find_status_ = FindStatus::EmptyList;
            return;
        }
        auto temp_cursor = cursor_->nextNode;
        while (temp_cursor and temp_cursor->value != value) {
            temp_cursor = temp_cursor->nextNode;
        }
        if (temp_cursor) {
            cursor_ = temp_cursor;
            find_status_ = FindStatus::Ok;
            return;
        }
        find_status_ = FindStatus::NotFound;
    }
    void remove_all(T value) override
    {
        head();
        while (not is_tail()) {
            if (get() == value)
                remove();
            right();
        }
        if (get() == value)
            remove();
    }
    T get() const override
    {
        if (not is_value()) {
            get_status_ = GetStatus::EmptyList;
            return T {};
        }
        get_status_ = GetStatus::Ok;
        return cursor_->value;
    }
    unsigned int size() const override
    {
        unsigned int nodeCount = 0;

        auto temp_cursor = head_;
        while (temp_cursor) {
            ++nodeCount;
            temp_cursor = temp_cursor->nextNode;
        }

        return nodeCount;
    }
    bool is_head() const override
    {
        return is_value() and cursor_ == head_;
    }
    bool is_tail() const override
    {
        return is_value() and cursor_ == tail_;
    }
    bool is_value() const override
    {
        return head_ != nullptr;
    }

    HeadStatus get_head_status() const override
    {
        return head_status_;
    }
    TailStatus get_tail_status() const override
    {
        return tail_status_;
    }
    PutRightStatus get_put_right_status() const override
    {
        return put_right_status_;
    }
    PutLeftStatus get_put_left_status() const override
    {
        return put_left_status_;
    }
    RemoveStatus get_remove_status() const override
    {
        return remove_status_;
    }
    ReplaceStatus get_replace_status() const override
    {
        return replace_status_;
    }
    FindStatus get_find_status() const override
    {
        return find_status_;
    }
    GetStatus get_get_status() const override
    {
        return get_status_;
    }
    RightStatus get_right_status() const override
    {
        return right_status_;
    }

protected:
    struct Node {
        T value;
        Node* prevNode = nullptr;
        Node* nextNode = nullptr;

        Node(T v)
            : value(v)
        {
        }
    };

protected:
    Node* head_ = nullptr;
    Node* tail_ = nullptr;
    Node* cursor_ = nullptr;

    HeadStatus head_status_ = HeadStatus::NotCalled;
    TailStatus tail_status_ = TailStatus::NotCalled;
    PutRightStatus put_right_status_ = PutRightStatus::NotCalled;
    PutLeftStatus put_left_status_ = PutLeftStatus::NotCalled;
    RemoveStatus remove_status_ = RemoveStatus::NotCalled;
    ReplaceStatus replace_status_ = ReplaceStatus::NotCalled;
    FindStatus find_status_ = FindStatus::NotCalled;
    mutable GetStatus get_status_ = GetStatus::NotCalled;
    RightStatus right_status_ = RightStatus::NotCalled;
};

template <class T>
class LinkedList : public ParentLinkedList<T> {
};

template <class T>
class TwoWayList : public ParentLinkedList<T>, public AbstractTwoWayList<T> {
public:
    void left() override
    {
        if (not ParentLinkedList<T>::is_value()) {
            left_status_ = LeftStatus::EmptyList;
            return;
        }
        if (ParentLinkedList<T>::is_head()) {
            left_status_ = LeftStatus::CursorOnHead;
            return;
        }

        ParentLinkedList<T>::cursor_ = ParentLinkedList<T>::cursor_->prevNode;
        left_status_ = LeftStatus::Ok;
    }
    LeftStatus get_left_status() const override
    {
        return left_status_;
    }

private:
    LeftStatus left_status_ = LeftStatus::NotCalled;
};

} // end of namespace linked_list
