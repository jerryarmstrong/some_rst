src/components/Icon.tsx
=======================

Last edited: 2023-07-18 16:28:32

Contents:

.. code-block:: tsx

    interface Props {
  img: string;
  className?: string;
  alt?: string;
}

const Icon = ({ img, className, alt }: Props) => {
  return (
    <img
      src={`/icons/${img}.png`}
      className={className}
      width={16}
      height={16}
      alt={alt}
    />
  );
};

export default Icon;


