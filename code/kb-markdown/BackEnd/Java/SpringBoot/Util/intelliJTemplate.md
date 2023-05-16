```java


#if (${PACKAGE_NAME} && ${PACKAGE_NAME} != "")package ${PACKAGE_NAME};#end
#set( $CamelCaseName = "$NAME.substring(0,1).toLowerCase()$NAME.substring(1)" )

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;


import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;

import org.springframework.beans.factory.annotation.Value;

import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Objects;


@Service
@Slf4j
@RequiredArgsConstructor
public class ${NAME}ServiceImpl implements ${NAME}Service{
  
    
  @Value("${upload.dir}")
    public String uploadDir;

    @Override
    public String uploadFiles(MultipartFile file) {
        Path copyLocation;

        String fileName = file.getOriginalFilename();
        copyLocation = Paths.get(uploadDir + File.separator + StringUtils.cleanPath(Objects.requireNonNull(fileName)));

        try {
            Files.copy(file.getInputStream(), copyLocation);
            return copyLocation.toString();
        } catch (FileAlreadyExistsException e) {
            String[] arr = fileName.split("\\.");
            String finalFileName = arr[0] + "_" + System.currentTimeMillis() + "." + arr[1];
            copyLocation = Paths.get(uploadDir + File.separator + StringUtils.cleanPath(finalFileName));

            try {
                Files.copy(file.getInputStream(), copyLocation);
            } catch (IOException ioException) {
                ioException.printStackTrace();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return copyLocation.toString();

    }
}

```

```java
#if (${PACKAGE_NAME} && ${PACKAGE_NAME} != "")package ${PACKAGE_NAME};#end
#set( $CamelCaseName = "$NAME.substring(0,1).toLowerCase()$NAME.substring(1)" )

import org.springframework.web.multipart.MultipartFile;


public interface ${NAME}Service {
    String uploadFiles(MultipartFile file);
}
```