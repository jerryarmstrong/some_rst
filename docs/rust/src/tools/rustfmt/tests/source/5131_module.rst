src/tools/rustfmt/tests/source/5131_module.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-imports_granularity: Module

#![allow(dead_code)]

mod a {
    pub mod b {
        pub struct Data {
            pub a: i32,
        }
    }

    use crate::a::b::Data;
    use crate::a::b::Data as Data2;

    pub fn data(a: i32) -> Data {
        Data { a }
    }

    pub fn data2(a: i32) -> Data2 {
        Data2 { a }
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        pub fn test() {
            data(1);
            data2(1);
        }
    }
}


