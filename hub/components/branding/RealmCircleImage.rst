hub/components/branding/RealmCircleImage.tsx
============================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import image from './logoimage.png';

type Props = React.ImgHTMLAttributes<HTMLImageElement>;

export function RealmCircleImage(props: Props) {
  return <img {...props} src={image.src} />;
}


