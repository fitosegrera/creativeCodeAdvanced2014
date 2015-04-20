import ddf.minim.analysis.*;
import ddf.minim.*;

Minim       minim;
AudioInput  in;
FFT         fft;
float[] fftReal;
float[] fftImag;
int specSize;
void setup() {
  size(640, 360, P3D);
  minim = new Minim(this);
  in = minim.getLineIn(Minim.MONO, 1024);
  fft = new FFT(in.bufferSize(), in.sampleRate());
  specSize = fft.specSize();
  fftReal   = new float[specSize];
}

void draw() {
  background(0);
  stroke(255);

  fft.forward( in.left);
  fftReal = fft.getSpectrumReal();
  for (int i = 0; i < specSize; i++) {
    float band = fft.getBand(i);
    if (fftReal[i] < band) fftReal[i] = band;
    stroke(255, 255, 255);
    line( i, height, i, height - fftReal[i]*8 );
    //stroke(i,100,100);
    //line( i, height, i, height - band*8 );
  }
}
