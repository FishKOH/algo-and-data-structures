Пред- и пост-условия верны, интуитивно легко определяются.  
Из минусов: 
- поспешил и не определил АТД, а сразу реализовал АТД в виде класса.
- забыл `const` у метода-запроса `peek()`

Привожу определение АТД с псевдо-конструктором(в С++ нельзя определить виртуальный конструктор):
```cpp
template <class T>
class AbstractBoundedStack {
public:
enum class PeekStatus {
    NotCalled,
    Ok,
    EmptyStack
};
enum class PopStatus {
    NotCalled,
    Ok,
    EmptyStack
};
enum class PushStatus {
    NotCalled,
    Ok,
    OverflowStack
};

public:
    //постусловие: создан новый пустой стек
    // конструктор
    // virtual AbstractBoundedStack(unsigned int maxSize) = 0;

    //предусловие: размер стека меньше максимального размера
    //постусловие: в стек добавлено новое значение
    virtual void push(T value) = 0;

    //предусловие: стек не пустой
    //постусловие: из стека удалён верхний элемент
    virtual void pop() = 0;

    //постусловие: из стека удалены все элементы
    virtual void clear() = 0;

    //предусловие: стек не пустой
    virtual T peek() const = 0;

    virtual int size() const = 0;

    virtual PeekStatus getPeekStatus() const = 0;
    virtual PopStatus getPopStatus() const = 0;
    virtual PushStatus getPushStatus() const = 0;
};
```
