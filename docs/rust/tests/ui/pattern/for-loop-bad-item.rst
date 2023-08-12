tests/ui/pattern/for-loop-bad-item.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Qux(i32);

fn bad() {
    let mut map = std::collections::HashMap::new();
    map.insert(('a', 'b'), ('c', 'd'));

    for ((_, _), (&mut c, _)) in &mut map {
    //~^ ERROR mismatched types
        if c == 'e' {}
    }
}

fn bad2() {
    for Some(Qux(_)) | None in [Some(""), None] {
    //~^ ERROR mismatched types
        todo!();
    }
}

fn main() {}


