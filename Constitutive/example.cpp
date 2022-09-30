// ---------------Name: StarDEM -------------------
// ------------Author: Chengshun Shang-------------
// -----------------Date: 04-01-2022---------------
// ---------------License : BSD license------------

#include <pybind11/pybind11.h>

namespace py = pybind11;

int add(int i = 1, int j = 2){
    return i+j;
}

class Pet{
public:
    Pet(const std::string &name) : name(name){ }
    void setName(const std::string &name_) {
        name = name_;
    }
    const std::string &getName() const{
        return name;
    }
//private:
    std::string name;
};

struct Animal{
//public:
    Animal(const std::string &name) : name(name){ }
    virtual ~Animal() = default;
    std::string name;
};

struct Dog : Animal{
//public:
    Dog(const std::string &name) : Animal(name) { }
    std::string bark() const{
        return "woof!";
    }
};

struct PolymorphicPet{
    virtual ~PolymorphicPet() = default;
};

struct PolymorphicDog : PolymorphicPet{
    std::string bark() const {
        return "woof!";
    }
};

struct Pet2{
    Pet2(const std::string &name, int age): name(name), age(age) { }

    void set(int age_) { age = age_;}
    void set(const std::string &name_) { name = name_;}

    std::string name;
    int age;
};

struct Widget{
    int foo(int x, float y);
    int foo(int x, float y) const;
};

PYBIND11_MODULE(StarDEM, m){
    m.doc() = "pybind11 example plugin";
    //regular notation
    m.def("add1", &add, "A function that add two numbers", py::arg("i") = 1, py::arg("j") = 2);
    //shorthand
    using namespace pybind11::literals;
    m.def("add2", &add, "A function that add two numbers v2", "i"_a, "j"_a);

    m.attr("the_answer") = 42;
    m.attr("warning") = "keep away!";

    py::object world = py::cast("WWWWWWorld");
    m.attr("what") = world;

    // bindings for C++ struct or class
    py::class_<Pet>(m, "Pet", py::dynamic_attr())
        .def(py::init<const std::string &>())
        //.def(py::init<>())
        .def("setName", &Pet::setName)
        .def("getName", &Pet::getName)
        //.def_property("name", &Pet::getName, &Pet::setName);
        //.def("__repr__",
        //    [](const Pet &a){
        //        return "<example.Pet named '" + a.name + "'>";
        //    }
        //)
        .def_readwrite("name", &Pet::name);

    //////////////////////////////////////////////////////////
    py::class_ <Animal> (m, "Animal")
        .def(py::init<const std::string &>())
        .def_readwrite("name", &Animal::name);

    py::class_ <Dog, Animal> (m, "Dog")
        .def(py::init<const std::string &>())
        .def("bark", &Dog::bark);

    // retuen a base pointer to a derived instance
    m.def("animal_store", []() {
        return std::unique_ptr<Animal>(new Dog("Dabai"));
    });

    //binding code/////////////////////////////////////////
    py::class_<PolymorphicPet>(m, "PolymorphicPet");
    py::class_<PolymorphicDog, PolymorphicPet>(m, "PolymorphicDog")
        .def(py::init<>())
        .def("bark", &PolymorphicDog::bark);

    m.def("pet_store2", [](){
        return std::unique_ptr<PolymorphicPet>(new PolymorphicDog);
    });

    ///////////////////////////////////////////////////////
    py::class_<Pet2>(m, "Pet2")
        .def(py::init<const std::string &, int>())
        .def("set", static_cast<void (Pet2::*)(int)>(&Pet2::set), "Set the pet's age")
        .def("set", static_cast<void (Pet2::*)(const std::string &)>(&Pet2::set), "set the pet's name");

    ///////////////////////////////////////////////////////
    /*
    py::class_<Widget>(m, "Widget")
        .def("foo_mutable", py::overload_cast<int, float>(&Widget::foo))
        .def("foo_const", py::overload_cast<int, float>(&Widget::foo, py::const_)); */
}