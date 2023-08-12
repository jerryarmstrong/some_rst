tests/incremental/change_private_fn_cc/auxiliary/point.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Point {
    pub x: f32,
    pub y: f32,
}

fn distance_squared(this: &Point) -> f32 {
    #[cfg(cfail1)]
    return this.x + this.y;

    #[cfg(cfail2)]
    return this.x * this.x + this.y * this.y;
}

impl Point {
    pub fn distance_from_origin(&self) -> f32 {
        distance_squared(self).sqrt()
    }
}

impl Point {
    pub fn translate(&mut self, x: f32, y: f32) {
        self.x += x;
        self.y += y;
    }
}


