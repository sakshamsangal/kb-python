
```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>

    <property name="HOME_LOG" value="logs/app.log"/>

    <appender name="FILE-ROLLING" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>log</file>

        <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
            <fileNamePattern>logs/archived/app.%d{yyyy-MM-dd}.%i.log.gz</fileNamePattern>
            <!-- each archived file, size max 10MB -->
            <maxFileSize>10MB</maxFileSize>
            <!-- total size of all archive files, if total size > 20GB, it will delete old archived file -->
            <totalSizeCap>20GB</totalSizeCap>
            <!-- 60 days to keep -->
            <maxHistory>60</maxHistory>
        </rollingPolicy>

        <encoder>
            <pattern>%d %p %c{1.} [%t] %m%n</pattern>
        </encoder>
    </appender>

    <logger name="com.mkyong" level="debug" additivity="false">
        <appender-ref ref="FILE-ROLLING"/>
    </logger>

    <root level="error">
        <appender-ref ref="FILE-ROLLING"/>
    </root>

</configuration>

```
```

package com.javacodegeeks.examples.logbackencoderexample;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ApplicationStarter3 {

	private static final Logger	logger	= LoggerFactory.getLogger( "sizeAndTimeBased" );

	public static void main( final String[] args ) {

		for ( int i = 1; i <= 40; i++ ) {
			logger.info( "write log with SizeAndTimeBasedFNATP" );

			try {
				Thread.sleep( 1000L );
			} catch ( final InterruptedException e ) {
				logger.error( "an error occurred", e );
			}
		}
	}
}

## logback.xml

<?xml version="1.0" encoding="UTF-8"?>
<configuration>
	<appender name="SIZE_AND_TIME_BASED_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
		<file>c:/logs/archived/app.log</file>
		<rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
			
			<!-- every second -->
			<fileNamePattern>c:/logs/archived/app_%d{yyy_MM_dd HH_mm_ss}_%i.log</fileNamePattern>
			<timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
				<maxFileSize>10KB</maxFileSize>
			</timeBasedFileNamingAndTriggeringPolicy>
		</rollingPolicy>
		<encoder>
			<pattern>%d{yyyy-MM-dd HH:mm:ss} - %msg%n</pattern>
		</encoder>
	</appender>
	<logger name="sizeAndTimeBased" level="INFO">
		<appender-ref ref="SIZE_AND_TIME_BASED_FILE" />
	</logger>
</configuration>


```

