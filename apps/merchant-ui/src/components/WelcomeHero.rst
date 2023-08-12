apps/merchant-ui/src/components/WelcomeHero.tsx
===============================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: tsx

    import Image from 'next/image';
import { twMerge } from 'tailwind-merge';

interface Props {
    className?: string;
}

export function WelcomeHero(props: Props) {
    return (
        <Image
            className={twMerge(props.className)}
            src="/solana_pay_hero.svg"
            alt="Welcome to Solana Pay"
            width={400}
            height={1000}
        />
    );
}


