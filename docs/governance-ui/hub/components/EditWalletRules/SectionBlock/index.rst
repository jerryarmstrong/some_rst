hub/components/EditWalletRules/SectionBlock/index.tsx
=====================================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import cx from '@hub/lib/cx';

interface Props {
  className?: string;
  children: React.ReactNode;
}

export function SectionBlock(props: Props) {
  return (
    <section
      className={cx(
        props.className,
        'p-8',
        'pt-5',
        'rounded',
        'dark:bg-black/40',
      )}
    >
      {props.children}
    </section>
  );
}


