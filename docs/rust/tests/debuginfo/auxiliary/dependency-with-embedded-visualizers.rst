tests/debuginfo/auxiliary/dependency-with-embedded-visualizers.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-g
// ignore-lldb
// no-prefer-dynamic

#![feature(debugger_visualizer)]
#![debugger_visualizer(natvis_file = "dependency-with-embedded-visualizers.natvis")]
#![debugger_visualizer(gdb_script_file = "dependency-with-embedded-visualizers.py")]
#![crate_type = "rlib"]

pub struct Person {
    name: String,
    age: i32,
}

impl Person {
    pub fn new(name: String, age: i32) -> Person {
        Person { name: name, age: age }
    }
}


