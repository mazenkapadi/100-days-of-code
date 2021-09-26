float x = 0;
float y = 0;

void setup()    {
    size(600,600);
        //beginRecord(PDF,"mandala.pdf");
    x = width/2;
    y = height/2;
}

void draw()    {
    background(0);
    strokeWeight(3);
    stroke(#8B7C26);
    pushMatrix();

    translate(x,y);
    rotate(radians(map(mouseX,0,width,0,360)));     //shapes below all rotate in unison
    translate(-x,-y);
    translate(x,y);
    fill(0);
    star(0,0, 260, 280,20);
    translate(-x,-y);
    translate(x,y);
    fill(#03A550);
    star(0,0, 250, 270, 20);
    translate(-x,-y);
    fill(#065F4A);
    ellipseMode(CENTER);
    ellipse(300,300,500,500);
    translate(x,y);
    fill(#0F9071);
    star(0,0, 230, 250, 40);
    translate(-x,-y);
    fill(#0C979B);
    ellipse(300,300,460,460);
    translate(x,y);
    fill(#1470B4);
    polygon(0, 0, 210, 8);      //octagon
    fill(#141DB4);
    polygon(0, 0, 190, 8);      //octagon
    translate(-x,-y);
    popMatrix();

    pushMatrix();
    translate(x,y);
    rotate(radians(map(mouseX,0,width,360,0)));     //reverse the rotation
    translate(-x,-y);
    fill(#0B0E71);
    ellipse(300,300,270,270);
    translate(x,y);
    fill(#3D0476);

    star(0,0, 110, 160, 10);
    translate(-x,-y);

    translate(x,y);
    fill(#562483);
    star(0,0, 90, 140, 10);
    translate(-x,-y);
    translate(x,y);
    fill(#71148E);
    polygon(0,0,75,10);
    translate(-x,-y);
    translate(x,y);
    fill(#962DA5);
    star(0,0, 40,105, 10);
    translate(-x,-y);
    fill(#9B3583);
    ellipse(300,300,100,100);
    translate(x,y);
    fill(#90146B);
    star(0,0,30,42,12);
    translate(-x,-y);
    translate(x,y);
    fill(#71092F);
    polygon(0,0,24,8);
    translate(-x,-y);
    fill(#580104);
    ellipse(300,300,20,20);
    popMatrix();
}

void star(float x, float y, float radius1, float radius2, int npoints)    {
    float angle = TWO_PI / npoints;
    float halfAngle = angle/2.0;
    beginShape();
    for (float a = 0; a < TWO_PI; a += angle)   {
        float sx = x + cos(a) * radius2;
        float sy = y + sin(a) * radius2;
        vertex(sx, sy);
        sx = x + cos(a+halfAngle) * radius1;
        sy = y + sin(a+halfAngle) * radius1;
        vertex(sx, sy);
    }
    endShape(CLOSE);
}

void polygon(float x, float y, float radius, int npoints)    {
    float angle = TWO_PI / npoints;
    beginShape();
    for (float a = 0; a < TWO_PI; a += angle)    {
        float sx = x + cos(a) * radius;
        float sy = y + sin(a) * radius;
        vertex(sx, sy);
    }
    endShape(CLOSE);
        //endRecord();
}

