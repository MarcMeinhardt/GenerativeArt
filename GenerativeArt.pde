// Author : Marc Meinhardt
// Build Date : 09.20.2021
// Title : Generative Art

PImage chunk;

void setup() {
  size(1024,1024);
  String imgString = "chunk1.jpg";
  chunk = loadImage(imgString);
}

void draw() {
  
  //background(0);
  //image(chunk,0,0);
  
  loadPixels();
  chunk.loadPixels();
  
  for (int x = 0; x < width - 1; x++) {
    
    for (int y = 0; y < height; y++) {
      
      int loc = x + y * width;
      
      //float r = red(chunk.pixels[loc]);
      //float g = green(chunk.pixels[loc]);
      //float b = blue(chunk.pixels[loc]);
      
      //pixels[loc] = chunk.pixels[loc];
      
      //pixels[loc] = color(g,b,r);
      
      // MARKUP - : Choose which part of the image to apply filter in
        //if (x < 200 && x > 0) {
        //  pixels[loc] = color(g,b,r*2);
        //} else if (x > 400) {
        //  pixels[loc] = color(g,b,r);
        //} else {
        //  pixels[loc] = color(r,g,b);
        //}
        
      // MARKUP - : Highlight image based on mouse position
        //float d = dist(mouseX, mouseY, x, y);
        //float factor = map(d, 0, 200, 2, 0);
        //pixels[loc] = color (r*factor, g*factor, b*factor);
      
      // MARKUP - : Brightness
        //float bright = brightness(chunk.pixels[loc]);
        //if ( bright > 200) {
        //  pixels[loc] = color(255);
        //} else if (bright <= 200 && bright >= 100) {
        //  pixels[loc] = color(155);
        //} else {
        //  pixels[loc] = color(0);
        //}
      
      // MARKUP - : Brightness based on mouse X value
        //if ( b > mouseX) {
        //  pixels[loc] = color(255);
        //} else {
        //  pixels[loc] = color(0);
        //}
      
      // MARKUP - : Pixel Neighbors
        int loc1 = x + y * width;
        int loc2 = ( x + 1 ) + y * width;
        
        float b1 = brightness(chunk.pixels[loc1]);
        float b2 = brightness(chunk.pixels[loc2]);
        float diff = abs(b1-b2);
        
        //pixels[loc1] = color(diff);
        if (diff > 20) {
          pixels[loc1] = color(255);
        } else {
          pixels[loc1] = color(0);
        }
        
    } 
    
  }
  
  updatePixels();
  
}
