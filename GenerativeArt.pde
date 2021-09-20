// Author : Marc Meinhardt
// Build Date : 09.20.2021
// Title : Generative Art

PImage chunk1;

void setup() {
  size(1024,1024);
  String imgString = "chunk1.jpg";
  chunk1 = loadImage(imgString);
}

void draw() {
  
  //background(0);
  //image(chunk1,0,0);
  loadPixels();
  chunk1.loadPixels();
  
  for (int x = 0; x < width; x++) {
    
    for (int y = 0; y < height; y++) {
      
      int loc = x + y * width;
      pixels[loc] = chunk1.pixels[loc];
      
    } 
    
  }
  
  updatePixels();
  
}
