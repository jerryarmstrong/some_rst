tests/ui/codemap_tests/tab.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // ignore-tidy-tab

fn main() {
	bar; //~ ERROR cannot find value `bar`
}

fn foo() {
	"bar			boo" //~ ERROR mismatched types
}


