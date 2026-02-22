Sam remains confident that an obscured password file is still the best idea, but he screwed up with the calendar program. Sam has saved the unencrypted password file in /var/www/hackthissite.org/html/missions/basic/8/
However, Sam's young daughter Stephanie has just learned to program in PHP. She's talented for her age, but she knows nothing about security. She recently learned about saving files, and she wrote a script to demonstrate her ability.

Tantangan ini menggunakan SSI injection dapat diketahui dari requirement tantangan ini 
<img width="805" height="333" alt="image" src="https://github.com/user-attachments/assets/e0a42a3d-83b2-4f19-88b9-0e7571d23f06" />
1. memasukkan input untuk injection yaitu
  ```bash
   <!--#exec cmd="ls" -->
  ```
<img width="1849" height="266" alt="image" src="https://github.com/user-attachments/assets/428571e3-a900-45dc-b240-0fa46b0c6198" />

  setelah itu akan terdapat output yaitu file file shtml yang jika kita coba satu satu tidak ada yang bisa diakses
  2. Mencoba naik satu dengan 
   ```bash
   <!--#exec cmd="ls ../" -->
  ```
setelah dijalankan akan terlihat beberapa directory yang ada seperti yang nampak dibawah ini :
<img width="1544" height="455" alt="image" src="https://github.com/user-attachments/assets/231faab4-f14a-490d-86bb-0782c67e22d7" />

3. mencoba mengakses  au12ha39vc.php  dengan menambahkan nya pada url level 8 menjadi https://www.hackthissite.org/missions/basic/8/au12ha39vc.php dan didapat password nya adlaah
   **cae4ee54**
