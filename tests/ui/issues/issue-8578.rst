tests/ui/issues/issue-8578.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]
#![allow(non_upper_case_globals)]
// pretty-expanded FIXME #23616

pub struct UninterpretedOption_NamePart {
    name_part: Option<String>,
}

impl<'a> UninterpretedOption_NamePart {
    pub fn default_instance() -> &'static UninterpretedOption_NamePart {
        static instance: UninterpretedOption_NamePart = UninterpretedOption_NamePart {
            name_part: None,
        };
        &instance
    }
}

pub fn main() {}


