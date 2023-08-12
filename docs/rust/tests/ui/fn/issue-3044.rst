tests/ui/fn/issue-3044.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let needlesArr: Vec<char> = vec!['a', 'f'];
    needlesArr.iter().fold(|x, y| {
        //~^ ERROR this method takes 2 arguments but 1 argument was supplied
    });
}


