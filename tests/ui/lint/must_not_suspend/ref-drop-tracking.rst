tests/ui/lint/must_not_suspend/ref-drop-tracking.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// compile-flags: -Zdrop-tracking
#![feature(must_not_suspend)]
#![deny(must_not_suspend)]

#[must_not_suspend = "You gotta use Umm's, ya know?"]
struct Umm {
    i: i64
}

struct Bar {
    u: Umm,
}

async fn other() {}

impl Bar {
    async fn uhoh(&mut self) {
        let guard = &mut self.u; //~ ERROR `Umm` held across

        other().await;

        *guard = Umm {
            i: 2
        }
    }
}

fn main() {
}


