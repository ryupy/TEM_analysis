run("8-bit");
//run("Brightness/Contrast...");
run("Enhance Contrast", "saturated=0.35");
run("Apply LUT");
setAutoThreshold("Default dark");
//setThreshold(131, 255);
run("Convert to Mask");
run("Analyze Particles...", "size=0.005-0.01 display exclude clear include add");
