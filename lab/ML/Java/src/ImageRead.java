
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import javax.imageio.ImageIO;

public class ImageRead {

	public final static int WIDTH = 28;
	public final static int HIGTH = 28;

	public static void main(String[] args) throws IOException {
		for (int m = 0; m < 10; m++) {
			for (int n = 1; n <= 5000; n++) {
				BufferedImage startImage = (BufferedImage) ImageIO
						.read(new File("D:/MNIST/trainimage/pic2/" + m + "/" + n + ".bmp"));

				BufferedImage resizedImage = new BufferedImage(WIDTH, HIGTH, BufferedImage.TYPE_INT_ARGB);
				Graphics2D g = resizedImage.createGraphics();
				g.drawImage(startImage, 0, 0, WIDTH, HIGTH, null);
				g.dispose();

				BufferedImage binImage = new BufferedImage(WIDTH, HIGTH, BufferedImage.TYPE_BYTE_BINARY);

				for (int i = 0; i < WIDTH; i++) {
					for (int j = 0; j < HIGTH; j++) {
						int rgb = resizedImage.getRGB(i, j);
						binImage.setRGB(i, j, rgb);
					}
				}
				FileWriter fw = new FileWriter(new File("D:/traindata/" + m + "_" + n + ".txt"));
				BufferedWriter bw = new BufferedWriter(fw);
				for (int i = 0; i < WIDTH; i++) {
					for (int j = 0; j < HIGTH; j++) {
						int dip = binImage.getRGB(j, i);
						if (dip == -1) {
							bw.write("1");
						} else {
							bw.write("0");
						}
					}
					bw.write("\r\n");
				}
				bw.close();
			}

		}

	}

}
