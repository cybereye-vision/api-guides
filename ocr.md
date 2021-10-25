# Optical Character Recognition (OCR)

Tính năng nhận diện vùng ảnh có chứa ký tự và trích xuất nội dung. Nhận đầu vào là ảnh cần nhận diện, trả về kết quả là danh sách toạ độ vùng chứa ký tự trên ảnh và chuỗi ký tự của vùng ảnh đó.

Hiện tính năng OCR hỗ trợ tốt với 2 kiểu ký tự:

* Chữ in
* Chữ viết tay (tiếng Việt).

## Hướng dẫn

### Mô tả chung

Client gửi yêu cầu tới **AX Cloud Vision API** qua `Async HTTP request` và **AX Cloud Vision** sẽ kết quả trả về thông qua `http_callback_endpoint` mà phía client cung cấp.

![Mo_hinh_ket_noi](./assets/ocr-fig01.png)

* Client gửi request tới AX Cloud Vision API. AX trả về thông báo nhận yêu cầu thành công hoặc không thành công (trong trường hợp có lỗi nào đó xảy ra).
* Client nhận kết quả nhận dạng OCR thông qua `http_callback_endpoint` ngay khi AX Cloud Vision hoàn tất quá trình xử lý.

### Base64

**base64-encoded**: Ảnh cần được encode theo dạng base64 trước khi gửi yêu cầu.

Command line
```cmd
# Linux
$ base64 input.jpg > output.txt

# Mac OSX
$ base64 -i input.jpg -o output.txt
```

Python
```python
# Import the base64 encoding library.
import base64

# Pass the image data to an encoding function.
def encode_image(image):
  image_content = image.read()
  return base64.b64encode(image_content)
```

Java
```java
// Import the Base64 encoding library.
import org.apache.commons.codec.binary.Base64;

// Encode the image.
byte[] imageData = Base64.encodeBase64(imageFile.getBytes());
```

NodeJS
```js
// Read the file into memory.
var fs = require('fs');
var imageFile = fs.readFileSync('/path/to/file');

// Convert the image data to a Buffer and base64 encode it.
var encoded = Buffer.from(imageFile).toString('base64');
```

### HTTP callback

AX Cloud Vision sẽ chủ động trả về kết quả cho phía client ngay sau khi xử lý xong quá trình nhận dạng thông qua callback endpoint mà phía client cung cấp.

HTTP callback cần đảm bảo một số yêu cầu:

* Endpoint có dạng HTTP URL. Ví dụ: *http://example.com/callback/ocr*
* Protocol: `HTTP/HTTPS`
* Method: `POST`
* Header:
    - (**Required**) Content-Type: `application/json; charset=utf-8`
    - (*Optional*) Authorization: Bearer `<token>`
* Payload: chứa kết quả nhận dạng theo cấu trúc JSON

Ví dụ:
```json
{
    "response": <data>
}
```

> Hiện tại, AX Cloud Vision chưa hỗ trợ phía client tự chủ động đăng ký hàm callback, do đó client cần tự xây dựng và cung cấp endpoint (kèm `<token>` để xác thực nếu có) của HTTP callback với Cyber Eye để nhận được kết quả trả về.

### Request

Mỗi request tương ứng với 1 ảnh đầu vào cần xử lý.

* HTTP URL: `https://cloud.ocr.vn/v1/ocr:asyncAnnotate`
* HTTP method: `POST`
* HTTP header:
    - (**Required**) Content-Type: `application/json; charset=utf-8`
    - (**Required**) Authorization: Bearer `<API Key>`
* HTTP payload:
    - **image**: là ảnh sau khi đã encode dạng base64 ở bước trên.
    - **type**: `TEXT` nếu là chữ in, `HANDWRI` nếu là chữ viết tay.

#### Ví dụ

Payload chứa trong `request.json`

Chữ in

```json
{
  "request": {
      "image": "base64-encoded",
      "type": "TEXT"
    }
}
```

Chữ viết tay

```json
{
  "requests": {
      "image": "base64-encoded",
      "type": "HANDWRI",
      "languages": ["vi"]
    }
}
```
curl
```cmd
curl -X POST \
-H "Authorization: Bearer <API Key>" \
-H "Content-Type: application/json; charset=utf-8" \
-d @request.json \
"https://cloud.ocr.vn/v1/ocr:asyncAnnotate"
```

### Response

* HTTP status code:
    - `200 OK` nếu gửi yêu cầu thành công.
    - Mã lỗi khác kèm mô tả lỗi nếu gửi yêu cầu không thành công.

> Trường hợp gửi không thành công, client cần tự kiểm soát cơ chế retry. 

> AX Cloud Vision sẽ chỉ đối soát với những yêu cầu được gửi thành công. 