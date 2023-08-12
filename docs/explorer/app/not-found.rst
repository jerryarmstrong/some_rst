app/not-found.tsx
=================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import { ErrorCard } from '@components/common/ErrorCard';

export default function NotFoundPage() {
    return (
        <div className="container mt-n3">
            <ErrorCard text="Page not found" />
        </div>
    );
}


