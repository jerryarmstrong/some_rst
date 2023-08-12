app/components/common/LoadingArtPlaceholder.tsx
===============================================

Last edited: 2023-07-31 09:08:44

Contents:

.. code-block:: tsx

    import ContentLoader from 'react-content-loader';

export function LoadingArtPlaceholder() {
    return (
        <ContentLoader viewBox="0 0 212 200" height={150} width={150} backgroundColor="transparent">
            <circle cx="86" cy="100" r="8" />
            <circle cx="106" cy="100" r="8" />
            <circle cx="126" cy="100" r="8" />
        </ContentLoader>
    );
}


