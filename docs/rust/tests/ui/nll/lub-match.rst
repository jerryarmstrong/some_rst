tests/ui/nll/lub-match.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we correctly consider the type of `match` to be the LUB
// of the various arms, particularly in the case where regions are
// involved.

pub fn opt_str0<'a>(maybestr: &'a Option<String>) -> &'a str {
    match *maybestr {
        Some(ref s) => {
            let s: &'a str = s;
            s
        }
        None => "(none)",
    }
}

pub fn opt_str1<'a>(maybestr: &'a Option<String>) -> &'a str {
    match *maybestr {
        None => "(none)",
        Some(ref s) => {
            let s: &'a str = s;
            s
        }
    }
}

pub fn opt_str2<'a>(maybestr: &'a Option<String>) -> &'static str {
    match *maybestr {
        None => "(none)",
        Some(ref s) => {
            let s: &'a str = s;
            s
            //~^ ERROR lifetime may not live long enough
        }
    }
}

pub fn opt_str3<'a>(maybestr: &'a Option<String>) -> &'static str {
    match *maybestr {
        Some(ref s) => {
            let s: &'a str = s;
            s
            //~^ ERROR lifetime may not live long enough
        }
        None => "(none)",
    }
}

fn main() {}


