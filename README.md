## ClefNet: Recurrent Autoencoders with Dynamic Time Warping for Near-Lossless Music Compression and Minimal-Latency Transmission
Vignav Ramesh and Mason Wang

This is a TensorFlow implementation of the [ClefNet paper](https://arxiv.org):
```
Citation
```

### Resources

<table><tbody>
<!-- START TABLE -->
<!-- TABLE HEADER -->
<th valign="bottom">Resource</th>
<th valign="bottom">URL</th>
<!-- TABLE BODY -->
<tr>
<td align="center">Preprints.org</td>
<td align="center">Link</td>
</tr>
 <tr>
<td align="center">Full Paper (PDF)</td>
<td align="center">http://bit.ly/ClefNet-2021</td>
</tr>
  <tr>
<td align="center">Latent Space Web App</td>
<td align="center">https://latent-space.tech</td>
</tr>
 <tr>
<td align="center">Latent Space Video Demo</td>
<td align="center">https://latent-space.tech/demo</td>
</tr>
  <tr>
<td align="center">Latent Space GitHub Repo</td>
<td align="center">https://github.com/SwiftWinds/hackmit</td>
</tr>
</tbody></table>

### Abstract
The onset of coronavirus disease 2019 (COVID-19), an infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), has sparked unprecedented change. Due to the public health guidelines imposed during the COVID-19 pandemic, there is no longer sufficient street traffic for remaining buskers to generate sufficient revenue, leading a majority of street musicians to pursue remote music production. However, real-time music production is notoriously difficult due to the excessively high latencies that current video call platforms such as Zoom and Google Meet harbor. In this paper, we propose an architecture for a platform with end-to-end, near-lossless audio transmission tailored specifically to online joint music production, called Latent Space. We discuss the usage of a recurrent autoencoder with sequence-aware encoding (RAES) and a 1D convolutional layer for audio compression, which we dub ClefNet, as well as propose a new evaluation metric for naive autoencoders (AEs), MSE-DTW loss, which combines the traditional mean square error (MSE) loss function with dynamic time warping (DTW) to prevent an increase in loss when the target sequence predicted by the AE is strictly a temporal variation of the source sequence. Moreover, we detail the logistics of a live system implementation which uses the Web Audio API to extract raw audio samples in real-time to feed into our client-side model before relaying the traffic using peer-to-peer WebRTC technology. The Latent Space platform can be accessed at [https://latent-space.tech](https://latent-space.tech), and the code and data can be found under the MIT License at [https://github.com/rvignav/ClefNet](https://github.com/rvignav/ClefNet).

### Contributions
1. We propose an architecture for a platform with end-to-end, near-lossless audio transmission tailored specifically for online joint music production, called Latent Space. 
2. We discuss the usage of a recurrent autoencoder with sequence-aware encoding (RAES) and a 1D convolutional layer for audio compression, which we dub ClefNet.
3. We propose a new evaluation metric for naive autoencoders (AEs), MSE-DTW loss, which combines the traditional mean square error (MSE) loss function with dynamic time warping (DTW) to prevent an increase in loss when the target sequence predicted by the AE is strictly a temporal variation of the source sequence.
4. We detail the logistics of a live system implementation which uses the Web Audio API to extract raw audio samples in real-time to feed into our client-side model before relaying the traffic using peer-to-peer WebRTC technology.

### License
This project is under the MIT License. See [LICENSE](LICENSE) for details.
