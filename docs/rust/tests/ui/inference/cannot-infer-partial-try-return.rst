tests/ui/inference/cannot-infer-partial-try-return.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct QualifiedError<E>(E);

impl<E, T> From<E> for QualifiedError<T>
where
    E: std::error::Error,
    T: From<E>,
{
    fn from(e: E) -> QualifiedError<T> {
        QualifiedError(e.into())
    }
}

fn infallible() -> Result<(), std::convert::Infallible> {
    Ok(())
}

fn main() {
    let x = || -> Result<_, QualifiedError<_>> {
        infallible()?;
        Ok(())
        //~^ ERROR type annotations needed
    };
}


