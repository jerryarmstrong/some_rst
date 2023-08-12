tests/ui/borrowck/borrowck-issue-48962.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Node {
    elem: i32,
    next: Option<Box<Node>>,
}

fn a() {
    let mut node = Node {
        elem: 5,
        next: None,
    };

    let mut src = &mut node;
    {src};
    src.next = None; //~ ERROR use of moved value: `src` [E0382]
}

fn b() {
    let mut src = &mut (22, 44);
    {src};
    src.0 = 66; //~ ERROR use of moved value: `src` [E0382]
}

fn main() {
    a();
    b();
}


