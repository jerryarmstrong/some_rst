tests/incremental/add_private_fn_at_krate_root_cc/auxiliary/point.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Point {
    pub x: f32,
    pub y: f32,
}

#[cfg(rpass2)]
fn unused_helper() {
}

pub fn distance_squared(this: &Point) -> f32 {
    return this.x * this.x + this.y * this.y;
}

impl Point {
    pub fn distance_from_origin(&self) -> f32 {
        distance_squared(self).sqrt()
    }
}


