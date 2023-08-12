tests/ui/borrowck/issue-95079-missing-move-in-nested-closure.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo1(s: &str) -> impl Iterator<Item = String> + '_ {
    None.into_iter()
        .flat_map(move |()| s.chars().map(|c| format!("{}{}", c, s)))
        //~^ ERROR captured variable cannot escape `FnMut` closure body
        //~| HELP consider adding 'move' keyword before the nested closure
}

fn foo2(s: &str) -> impl Sized + '_ {
    move |()| s.chars().map(|c| format!("{}{}", c, s))
    //~^ ERROR lifetime may not live long enough
    //~| HELP consider adding 'move' keyword before the nested closure
}

fn main() {}


