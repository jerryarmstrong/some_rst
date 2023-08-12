src/components/DAOStructures/Card.tsx
=====================================

Last edited: 2023-07-18 16:28:32

Contents:

.. code-block:: tsx

    import Image from 'next/image';

import clsxm from '@/lib/clsxm';
import trackClick from '@/lib/trackClick';

import * as Anchor from '@/components/Anchor';
import Header from '@/components/Header';
import Icon from '@/components/Icon';
import Text from '@/components/Text';

export declare type AlignType = 'left' | 'center' | 'right';

interface Props {
  bg: string;
  bgAlignment: AlignType;
  className?: string;
  content: string;
  cta: {
    href: string;
    text: string;
  };
  daos: {
    icons: string[];
    text: string;
  };
  title: React.ReactNode;
  trackingContext: string;
  trackingLabel: string;
}

export default function Card(props: Props) {
  return (
    <article
      className={clsxm(
        props.className,
        'overflow-hidden',
        'px-5',
        'py-8',
        'relative',
        'rounded-md',
        'sm:p-8'
      )}
    >
      <div
        className={clsxm(
          '-z-10',
          'absolute',
          'bottom-0',
          'h-[450px]',
          'w-[800px]',
          props.bgAlignment === 'left' && 'left-0',
          props.bgAlignment === 'right' && 'right-0',
          props.bgAlignment === 'center' && 'left-1/2',
          props.bgAlignment === 'center' && '-translate-x-1/2'
        )}
      >
        <Image alt='background' layout='fill' src={props.bg} />
      </div>
      <div className='mb-5 flex items-center lg:min-h-[98px] 1_5xl:max-w-[360px]'>
        <Header as='h3'>{props.title}</Header>
      </div>
      <Text withOpacity className='block max-w-[489px] pb-8 lg:min-h-[104px]'>
        {props.content}
      </Text>
      <div className='mb-6 flex items-center gap-3'>
        <div className='flex shrink-0 -space-x-3'>
          {props.daos.icons.map((src) => (
            <img alt='icon' className='h-10 w-10' key={src} src={src} />
          ))}
        </div>
        <div className='max-w-[205px] text-xs opacity-50'>
          {props.daos.text}
        </div>
      </div>
      <Anchor.Dark
        className='w-full max-w-[356px] justify-between'
        href={props.cta.href}
        onClick={() => trackClick(props.trackingLabel, props.trackingContext)}
      >
        {props.cta.text}{' '}
        <Icon
          img='arrow-thin-blue'
          className={clsxm(
            'ml-4',
            'transition-all',
            'group-focus:brightness-0',
            'group-hover:brightness-0'
          )}
          alt='Arrow'
        />
      </Anchor.Dark>
    </article>
  );
}


