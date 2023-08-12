tests/ui/pattern/usefulness/type_polymorphic_byte_str_literals.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[deny(unreachable_patterns)]

fn parse_data1(data: &[u8]) -> u32 {
    match data {
        b"" => 1,
        _ => 2,
    }
}

fn parse_data2(data: &[u8]) -> u32 {
    match data { //~ ERROR non-exhaustive patterns: `&[_, ..]` not covered
        b"" => 1,
    }
}

fn parse_data3(data: &[u8; 0]) -> u8 {
    match data {
        b"" => 1,
    }
}

fn parse_data4(data: &[u8]) -> u8 {
    match data { //~ ERROR non-exhaustive patterns
        b"aaa" => 0,
        [_, _, _] => 1,
    }
}

fn parse_data5(data: &[u8; 3]) -> u8 {
    match data {
        b"aaa" => 0,
        [_, _, _] => 1,
    }
}

fn main() {}


