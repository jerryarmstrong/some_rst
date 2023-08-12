components/treasuryV2/WalletList/WalletListItem/AssetList/TokenOwnerRecordListItem.tsx
======================================================================================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: tsx

    import ListItem from './ListItem'

interface Props {
  className?: string
  onSelect?(): void
  name: string
  selected?: boolean
  thumbnail: JSX.Element
}
export default function TokenOwnerRecordListItem(props: Props) {
  return (
    <ListItem
      className={props.className}
      name={props.name}
      rhs={<></>}
      selected={props.selected}
      onSelect={props.onSelect}
      thumbnail={props.thumbnail}
    />
  )
}


