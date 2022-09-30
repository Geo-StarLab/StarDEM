
// System includes
#include <pybind11/pybind11.h>

#include "../Constitutive/mytest.h"

namespace py = pybind11;

namespace Star{

    PYBIND11_MODULE(StarDEM, m){

        //py::class_<StarDEM>(m, "StarDEM")
        //    .def(init<>());
        //    ;
        
        m.doc() = "pybind11 StarDEM plugin";

        py::class_<FirstTest>(m, "FirstTest")
            .def(py::init<>())
            .def("MyName", &FirstTest::MyName)
            ;

    }


}