import ddf.minim.spi.*;
import ddf.minim.signals.*;
import ddf.minim.*;
import ddf.minim.analysis.*;
import ddf.minim.ugens.*;
import ddf.minim.effects.*;

AudioInput in;
Minim minim;
float[] buffer;

void setup() {
  size(640, 480, P3D);
  minim = new Minim(this);

  in = minim.getLineIn(Minim.MONO, 1024);

  buffer = new float[in.bufferSize()];
}

void draw() {
  background(0);
  for (int i = 0; i < in.bufferSize(); i++) {
    buffer[i] = in.mix.get(i);
  }
  for (int i = 0; i < in.bufferSize(); i++) {
     float x1 = map(i, 0, in.bufferSize(), 0, width);
     float x2 = map(i + 1, 0, in.bufferSize(), 0, width);
     line(x1, buffer[i], x2, buffer[i+1]);
  }
}
