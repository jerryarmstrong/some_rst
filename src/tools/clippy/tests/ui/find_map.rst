src/tools/clippy/tests/ui/find_map.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::all, clippy::pedantic)]

#[derive(Debug, Copy, Clone)]
enum Flavor {
    Chocolate,
}

#[derive(Debug, Copy, Clone)]
enum Dessert {
    Banana,
    Pudding,
    Cake(Flavor),
}

fn main() {
    let desserts_of_the_week = vec![Dessert::Banana, Dessert::Cake(Flavor::Chocolate), Dessert::Pudding];

    let a = ["lol", "NaN", "2", "5", "Xunda"];

    let _: Option<i32> = a.iter().find(|s| s.parse::<i32>().is_ok()).map(|s| s.parse().unwrap());

    #[allow(clippy::match_like_matches_macro)]
    let _: Option<Flavor> = desserts_of_the_week
        .iter()
        .find(|dessert| match *dessert {
            Dessert::Cake(_) => true,
            _ => false,
        })
        .map(|dessert| match *dessert {
            Dessert::Cake(ref flavor) => *flavor,
            _ => unreachable!(),
        });
}


