tests/ui/rfc-2397-do-not-recommend/incorrect-locations.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(do_not_recommend)]

#[do_not_recommend]
//~^ `#[do_not_recommend]` can only be placed
const CONST: () = ();

#[do_not_recommend]
//~^ `#[do_not_recommend]` can only be placed
static Static: () = ();

#[do_not_recommend]
//~^ `#[do_not_recommend]` can only be placed
type Type = ();

#[do_not_recommend]
//~^ `#[do_not_recommend]` can only be placed
enum Enum {
}

#[do_not_recommend]
//~^ `#[do_not_recommend]` can only be placed
extern {
}

#[do_not_recommend]
//~^ `#[do_not_recommend]` can only be placed
fn fun() {
}

#[do_not_recommend]
//~^ `#[do_not_recommend]` can only be placed
struct Struct {
}

#[do_not_recommend]
//~^ `#[do_not_recommend]` can only be placed
trait Trait {
}

#[do_not_recommend]
impl Trait for i32 {
}

fn main() {
}


