src/tools/rustfmt/tests/target/issue-4152.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-hard_tabs: true

macro_rules! bit {
	($bool:expr) => {
		if $bool {
			1;
			1
		} else {
			0;
			0
		}
	};
}
macro_rules! add_one {
	($vec:expr) => {{
		$vec.push(1);
	}};
}


