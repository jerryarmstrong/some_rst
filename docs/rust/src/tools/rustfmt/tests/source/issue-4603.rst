src/tools/rustfmt/tests/source/issue-4603.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Formatting when original macro snippet is used

// Original issue #4603 code
#![feature(or_patterns)]
macro_rules! t_or_f {
    () => {
        (true // some comment
        | false)
    };
}

// Other test cases variations
macro_rules! RULES {
    () => {
        (
		xxxxxxx // COMMENT
        | yyyyyyy
        )
    };
}
macro_rules! RULES {
    () => {
        (xxxxxxx // COMMENT
            | yyyyyyy)
    };
}

fn main() {
	macro_rules! RULES {
		() => {
			(xxxxxxx // COMMENT
			| yyyyyyy)
		};
	}
}

macro_rules! RULES {
    () => {
        (xxxxxxx /* COMMENT */ | yyyyyyy)
    };
}
macro_rules! RULES {
    () => {
        (xxxxxxx /* COMMENT */
        | yyyyyyy)
    };
}


