tests/ui/codemap_tests/tab_3.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-tab

fn main() {
	let some_vec = vec!["hi"];
	some_vec.into_iter();
	{
		println!("{:?}", some_vec); //~ ERROR borrow of moved
	}
}


