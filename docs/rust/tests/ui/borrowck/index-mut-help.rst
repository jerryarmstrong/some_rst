tests/ui/borrowck/index-mut-help.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // When mutably indexing a type that implements `Index` but not `IndexMut`, a
// special 'help' message is added to the output.
use std::collections::HashMap;


fn main() {
    let mut map = HashMap::new();
    map.insert("peter", "23".to_string());

    map["peter"].clear();           //~ ERROR
    map["peter"] = "0".to_string(); //~ ERROR
    let _ = &mut map["peter"];      //~ ERROR
}


