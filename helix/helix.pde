int transX;
int numSpheres = 10;
Sphere s[] = new Sphere[numSpheres];

void setup() {
  transX = width/2;
  size(1024, 720, P3D);
  for (int i = 0; i < numSpheres; i++) {
    s[i] = new Sphere(30, 100, i*70, (PI/100+i+1)*0.01);
  }
}
void draw() {
  background(0);
  noStroke();
  lights();
  translate(transX, 50);
  for (int i = 0; i < numSpheres; i++) {
    fill(map(i, 0, numSpheres, 0, 255), 100, 0);
    s[i].draw();
  }
}
public class Sphere {
  int size, orbit, posY;
  float rotation = 0, rotRate;
  public Sphere(int size, int orbit, int posY, float rotRate) {
    this.size = size;
    this.posY = posY;
    this.orbit = orbit;
    this.rotRate = rotRate;
  } 
  public void draw() {
    pushMatrix();
    rotateY(rotation); 
    translate(orbit, posY);
    sphere(size);
    popMatrix();
    rotation = (rotation + rotRate) % (2 * PI);
  }
}
