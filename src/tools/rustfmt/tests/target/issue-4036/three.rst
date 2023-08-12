src/tools/rustfmt/tests/target/issue-4036/three.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-format_strings: true
// rustfmt-hard_tabs: true

macro_rules! test {
	() => {
		fn from() {
			None.expect(
				"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor \
				 incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis \
				 nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \
				 Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu \
				 fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in \
				 culpa qui officia deserunt mollit anim id est laborum.",
			)
		}
	};
}


