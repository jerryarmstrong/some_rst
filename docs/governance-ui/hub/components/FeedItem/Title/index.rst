hub/components/FeedItem/Title/index.tsx
=======================================

Last edited: 2023-05-19 22:20:18

Contents:

.. code-block:: tsx

    import cx from '@hub/lib/cx';

interface BaseProps {
  className?: string;
}

interface Props extends BaseProps {
  title: string;
}

export function Content(props: Props) {
  return (
    <h1
      className={cx(
        props.className,
        'text-2xl',
        'sm:text-4xl',
        'text-zinc-900',
        'font-bold',
      )}
    >
      {props.title}
    </h1>
  );
}

export function Error(props: BaseProps) {
  return (
    <div
      className={cx(
        props.className,
        'text-2xl',
        'sm:text-4xl',
        'w-96',
        'rounded',
        'bg-neutral-200',
      )}
    >
      &nbsp;
    </div>
  );
}

export function Loading(props: BaseProps) {
  return (
    <div
      className={cx(
        props.className,
        'text-2xl',
        'sm:text-4xl',
        'w-96',
        'rounded',
        'bg-neutral-200',
        'animate-pulse',
      )}
    >
      &nbsp;
    </div>
  );
}


