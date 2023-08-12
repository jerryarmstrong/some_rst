hub/components/branding/RealmCircleImage.tsx
============================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import image from './logoimage.png';

type Props = React.ImgHTMLAttributes<HTMLImageElement>;

export function RealmCircleImage(props: Props) {
  return <img {...props} src={image.src} />;
}


