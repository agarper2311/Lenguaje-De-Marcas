<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    
    <xsl:output method="html" encoding="UTF-8" indent="yes"/>
    
    <xsl:template match="/">
        <html>
            <head>
                <title>Lista de Libros</title>
                <style>
                    table {
                        border-collapse: collapse;
                        width: 100%;
                    }
                    th, td {
                        border: 1px solid black;
                        padding: 8px;
                        text-align: left;
                        background-color: #00bcc0;
                    }
                    th {
                        background-color: #00ffff;
                    }
                </style>
            </head>
            <body>
                <h1>Libros Disponibles</h1>
                <table>
                    <tr>
                        <th>Título</th>
                        <th>Editorial</th>
                        <th>Edición</th>
                        <th>ISBN</th>
                        <th>Núm. Páginas</th>
                        <th>Autores</th>
                    </tr>
                    <xsl:for-each select="Libros/libro">
                        <tr>
                            <td><xsl:value-of select="Titulo"/></td>
                            <td><xsl:value-of select="Editorial"/></td>
                            <td><xsl:value-of select="Edicion"/></td>
                            <td><xsl:value-of select="ISBN"/></td>
                            <td><xsl:value-of select="NumPaginas"/></td>
                            <td>
                                <xsl:for-each select="Autores/autor">
                                    <xsl:value-of select="concat(Nombre, ' ', Apellidos, ' (', Nacionalidad, ')')"/>
                                    <xsl:if test="position()!=last()">
                                        <br/>
                                    </xsl:if>
                                </xsl:for-each>
                            </td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>
