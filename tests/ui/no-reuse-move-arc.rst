tests/ui/no-reuse-move-arc.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::sync::Arc;
use std::thread;

fn main() {
    let v = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let arc_v = Arc::new(v);

    thread::spawn(move|| {
        assert_eq!((*arc_v)[3], 4);
    });

    assert_eq!((*arc_v)[2], 3); //~ ERROR borrow of moved value: `arc_v`

    println!("{:?}", *arc_v);
}


