tests/ui/pattern/usefulness/match-byte-array-patterns.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unreachable_patterns)]

fn main() {
    let buf = &[0, 1, 2, 3];

    match buf {
        b"AAAA" => {},
        &[0x41, 0x41, 0x41, 0x41] => {} //~ ERROR unreachable pattern
        _ => {}
    }

    match buf {
        &[0x41, 0x41, 0x41, 0x41] => {}
        b"AAAA" => {}, //~ ERROR unreachable pattern
        _ => {}
    }

    match buf {
        &[_, 0x41, 0x41, 0x41] => {},
        b"AAAA" => {}, //~ ERROR unreachable pattern
        _ => {}
    }

    match buf {
        &[0x41, .., 0x41] => {}
        b"AAAA" => {}, //~ ERROR unreachable pattern
        _ => {}
    }

    let buf: &[u8] = buf;

    match buf {
        b"AAAA" => {},
        &[0x41, 0x41, 0x41, 0x41] => {} //~ ERROR unreachable pattern
        _ => {}
    }

    match buf {
        &[0x41, 0x41, 0x41, 0x41] => {}
        b"AAAA" => {}, //~ ERROR unreachable pattern
        _ => {}
    }

    match buf {
        &[_, 0x41, 0x41, 0x41] => {},
        b"AAAA" => {}, //~ ERROR unreachable pattern
        _ => {}
    }

    match buf {
        &[0x41, .., 0x41] => {}
        b"AAAA" => {}, //~ ERROR unreachable pattern
        _ => {}
    }
}


