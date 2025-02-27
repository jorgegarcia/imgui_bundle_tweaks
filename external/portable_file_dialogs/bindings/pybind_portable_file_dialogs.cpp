// Part of ImGui Bundle - MIT License - Copyright (c) 2022-2024 Pascal Thomet - https://github.com/pthom/imgui_bundle
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "portable_file_dialogs/portable_file_dialogs.h"
namespace py = pybind11;


// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// <litgen_glue_code>  // Autogenerated code below! Do not edit!

// </litgen_glue_code> // Autogenerated code end
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

namespace pfd {
    std::vector<std::string> all_files_filter() {
        return {"All files", "*"};
    }
}


void py_init_module_portable_file_dialogs(py::module& m)
{
    using namespace pfd;
    auto default_wait_timeout = pfd::internal::default_wait_timeout;

    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    // <litgen_pydef> // Autogenerated code below! Do not edit!
    ////////////////////    <generated_from:portable_file_dialogs_simplified.h>    ////////////////////
    py::enum_<pfd::button>(m, "button", py::arithmetic(), "")
        .value("cancel", pfd::button::cancel, "")
        .value("ok", pfd::button::ok, "")
        .value("yes", pfd::button::yes, "")
        .value("no", pfd::button::no, "")
        .value("abort", pfd::button::abort, "")
        .value("retry", pfd::button::retry, "")
        .value("ignore", pfd::button::ignore, "");


    py::enum_<pfd::choice>(m, "choice", py::arithmetic(), "")
        .value("ok", pfd::choice::ok, "")
        .value("ok_cancel", pfd::choice::ok_cancel, "")
        .value("yes_no", pfd::choice::yes_no, "")
        .value("yes_no_cancel", pfd::choice::yes_no_cancel, "")
        .value("retry_cancel", pfd::choice::retry_cancel, "")
        .value("abort_retry_ignore", pfd::choice::abort_retry_ignore, "");


    py::enum_<pfd::icon>(m, "icon", py::arithmetic(), "")
        .value("info", pfd::icon::info, "")
        .value("warning", pfd::icon::warning, "")
        .value("error", pfd::icon::error, "")
        .value("question", pfd::icon::question, "");


    py::enum_<pfd::opt>(m, "opt", py::arithmetic(), "Additional option flags for various dialog constructors")
        .value("none", pfd::opt::none, "")
        .value("multiselect", pfd::opt::multiselect, "For file open, allow multiselect.")
        .value("force_overwrite", pfd::opt::force_overwrite, "For file save, force overwrite and disable the confirmation dialog.")
        .value("force_path", pfd::opt::force_path, " For folder select, force path to be the provided argument instead\n of the last opened directory, which is the Microsoft-recommended,\n user-friendly behaviour.");


    auto pyClassnotify =
        py::class_<pfd::notify>
            (m, "notify", "\n The notify widget\n")
        .def(py::init<const std::string &, const std::string &, pfd::icon>(),
            py::arg("title"), py::arg("message"), py::arg("_icon") = pfd::icon::info)
        .def("ready",
            &notify::ready, py::arg("timeout") = default_wait_timeout)
        .def("kill",
            &notify::kill)
        ;


    auto pyClassmessage =
        py::class_<pfd::message>
            (m, "message", "\n The message widget\n")
        .def(py::init<const std::string &, const std::string &, pfd::choice, pfd::icon>(),
            py::arg("title"), py::arg("text"), py::arg("_choice") = pfd::choice::ok_cancel, py::arg("_icon") = pfd::icon::info)
        .def("result",
            &message::result)
        .def("ready",
            &message::ready, py::arg("timeout") = default_wait_timeout)
        .def("kill",
            &message::kill)
        ;


    m.def("all_files_filter",
        pfd::all_files_filter);


    auto pyClassopen_file =
        py::class_<pfd::open_file>
            (m, "open_file", "\n The open_file, save_file, and open_folder widgets\n")
        .def(py::init<const std::string &, const std::string &, const std::vector<std::string> &, pfd::opt>(),
            py::arg("title"), py::arg("default_path") = "", py::arg("filters") = pfd::all_files_filter(), py::arg("options") = pfd::opt::none)
        .def("ready",
            &open_file::ready, py::arg("timeout") = default_wait_timeout)
        .def("kill",
            &open_file::kill)
        .def("result",
            &open_file::result)
        ;


    auto pyClasssave_file =
        py::class_<pfd::save_file>
            (m, "save_file", "")
        .def(py::init<const std::string &, const std::string &, const std::vector<std::string> &, pfd::opt>(),
            py::arg("title"), py::arg("default_path") = "", py::arg("filters") = pfd::all_files_filter(), py::arg("options") = pfd::opt::none)
        .def("ready",
            &save_file::ready, py::arg("timeout") = default_wait_timeout)
        .def("kill",
            &save_file::kill)
        .def("result",
            &save_file::result)
        ;


    auto pyClassselect_folder =
        py::class_<pfd::select_folder>
            (m, "select_folder", "")
        .def(py::init<const std::string &, const std::string &, pfd::opt>(),
            py::arg("title"), py::arg("default_path") = "", py::arg("options") = pfd::opt::none)
        .def("ready",
            &select_folder::ready, py::arg("timeout") = default_wait_timeout)
        .def("kill",
            &select_folder::kill)
        .def("result",
            &select_folder::result)
        ;
    ////////////////////    </generated_from:portable_file_dialogs_simplified.h>    ////////////////////

    // </litgen_pydef> // Autogenerated code end
    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
}
