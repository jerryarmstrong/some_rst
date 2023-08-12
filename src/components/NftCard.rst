src/components/NftCard.js
=========================

Last edited: 2022-08-19 17:27:27

Contents:

.. code-block:: js

    import React, {useEffect, useState} from 'react';
import {View, Text, Image, ActivityIndicator, StyleSheet} from 'react-native';

const NftCard = ({data, metaplex}) => {
  const [nftData, setNftData] = useState(null);

  useEffect(() => {
    const execute = async () => {
      const metadata = await metaplex.metadata(data.mint);
      setNftData({
        image: metadata.image,
        name: metadata.name,
        symbol: metadata.symbol,
      });
    };
    execute();
  }, [data, metaplex]);

  return (
    <View style={styles.card}>
      {nftData ? (
        <>
          <Image
            resizeMode="contain"
            style={styles.image}
            source={{uri: nftData.image}}
          />
          <Text style={styles.title}>{nftData.name}</Text>
          <Text
            numberOfLines={1}
            ellipsizeMode="middle"
            style={styles.publicKey}>
            {data.mint}
          </Text>
        </>
      ) : (
        <View style={styles.loadingView}>
          <ActivityIndicator size="large" color={'#fff'} />
        </View>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  card: {
    width: '50%',
    backgroundColor: '#292929',
    marginVertical: 8,
    marginHorizontal: 3,
    height: 290,
    borderRadius: 10,
    flex: 1,
    alignItems: 'center',
  },
  title: {
    fontSize: 20,
    marginBottom: 5,
    color: '#fff',
  },
  publicKey: {
    fontSize: 15,
    color: '#fff',
  },
  image: {
    width: 200,
    height: 200,
    marginBottom: 20,
    borderRadius: 10,
    overflow: 'hidden',
  },
  loadingView: {flex: 1, justifyContent: 'center', alignItems: 'center'},
});

export default NftCard;


